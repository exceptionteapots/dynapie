package config

import (
	_ "github.com/exceptionteapots/dynapie/daemon/logging"
	"github.com/spf13/viper"
)

var config *viper.Viper

func init() {
	config = viper.New()
	config.SetConfigName("daemon")
	config.SetConfigType("yaml")
	config.AddConfigPath("/etc/dynapie")

	err := config.ReadInConfig()
	if err != nil {
		// Log an error and exit
	}
}
