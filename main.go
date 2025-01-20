package main

import (
	"context"
	"fmt"
	"os"
	"strings"
	"time"

	"github.com/docker/docker/api/types"
	"github.com/docker/docker/api/types/container"
	"github.com/docker/docker/client"

	"github.com/117503445/goutils"

	"github.com/go-resty/resty/v2"
	"github.com/rs/zerolog/log"
)

const dirData = "./data"
const fileLocalSha = dirData + "/latest-sha"

func Fetch() {
	log.Info().Msg("Start fetch")
	

	info, err := os.Stat(dirData)
	if err != nil {
		if os.IsNotExist(err) {
			if err := os.Mkdir(dirData, os.ModePerm); err != nil {
				panic(err)
			}
		} else {
			panic(err)
		}
	} else {
		if !info.IsDir() {
			panic("./data is not a directory")
		}
	}

	client := resty.New()
	resp, err := client.R().
		EnableTrace().
		Get("https://vsc-server.unidrop.top/latest-sha")
	if err != nil {
		log.Error().Err(err).Msg("Failed to fetch latest-sha")
		return
	}

	latestSha := resp.String()

	localSha := ""
	
	if _, err := os.Stat(fileLocalSha); err == nil {
		localShaBytes, err := os.ReadFile(fileLocalSha)
		if err != nil {
			log.Error().Err(err).Msg("Failed to read local sha")
			return
		}
		localSha = string(localShaBytes)
	}

	log.Debug().Str("localSha", localSha).Str("latestSha", latestSha).Msg("")

	if localSha == latestSha {
		log.Info().Msg("No update")
		return
	}

	log.Info().Str("latestSha", latestSha).Msg("Update")

	// download https://vsc-server.unidrop.top/${latest-sha} to ${dirData}/${latest-sha}.tar.gz
	fileVscTemp := fmt.Sprintf("%s/%s.tar.gz.tmp", dirData, latestSha)
	_, err = client.R().
		EnableTrace().
		SetOutput(fileVscTemp).
		Get(fmt.Sprintf("https://vsc-server.unidrop.top/%s", latestSha))
	if err != nil {
		log.Error().Err(err).Msg("Failed to download vsc")
		return
	}

	fileVsc := fmt.Sprintf("%s/%s.tar.gz", dirData, latestSha)
	if err = os.Rename(fileVscTemp, fileVsc); err != nil {
		log.Error().Err(err).Msg("Failed to rename vsc")
		return
	}

	if err = os.WriteFile(fileLocalSha, []byte(latestSha), os.ModePerm); err != nil {
		log.Error().Err(err).Msg("Failed to write local sha")
		return
	}

}

func main() {
	goutils.InitZeroLog()

	go func() {
		log.Info().Msg("Start fetch loop")
		for {
			Fetch()
			time.Sleep(time.Hour)
		}
	}()

	log.Info().Msg("Hello, World!")

	apiClient, err := client.NewClientWithOpts(client.FromEnv)
	if err != nil {
		panic(err)
	}
	defer apiClient.Close()

	containers, err := apiClient.ContainerList(context.Background(), container.ListOptions{All: true})
	if err != nil {
		panic(err)
	}

	latestSha := ""
	if _, err := os.Stat(fileLocalSha); err == nil {
		localShaBytes, err := os.ReadFile(fileLocalSha)
		if err != nil {
			log.Error().Err(err).Msg("Failed to read local sha")
			return
		}
		latestSha = string(localShaBytes)
	}
	if latestSha == "" {
		log.Error().Msg("latestSha is empty")
		return
	}

	for _, ctr := range containers {
		if strings.Contains(ctr.Image, "dev") {
			fmt.Printf("%s %s (status: %s)\n", ctr.ID, ctr.Image, ctr.Status)
			// docker exec -it ${ctr.ID} /root/.vscode-server/bin/$sha/bin/code-server
			resp, err := apiClient.ContainerExecCreate(context.Background(), ctr.ID, types.ExecConfig{
				Cmd:          []string{fmt.Sprintf("/root/.vscode-server/bin/%s/bin/code-server", latestSha ), "--version"},
				AttachStdout: true,
				AttachStderr: true,
			})
			if err != nil {
				log.Error().Err(err).Msg("Failed to create exec")
				continue
			}
			log.Debug().Str("execID", resp.ID).Msg("")

			
		}
	}
}
