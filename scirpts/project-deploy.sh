#!/bin/bash

####################### PROJECT PARAMS #############################

export PROJECT_NAME="dadousceno"
export PROJECT_PATH=~/Nextcloud/Didier/python/dadou_sceno
export UTILS_PROJECT=~/Nextcloud/Didier/python/dadou_utils

export USER_HOST="s"
export ROOT_HOST="sr"
export RPI_IP="192.168.1.220"

export INSTALL_LIB="yes"
export SET_USB_AUDIO="yes"
#export ACTIVATE_I2C="yes"
export SET_BASHRC="yes"
export SET_VIMRC="yes"
export INSTALL_SERVICE="yes"
#export INSTALL_AUTOSTART="yes"
export SERVICE_NAME=sceno

####################################################################

export RPI_HOME=/home/didier
export LOCAL_HOME=~

export UTILS_PATH=$LOCAL_HOME/Nextcloud/Didier/python/dadou_utils
export UTILS_SCRIPTS=$UTILS_PATH/scripts/deploy

if [ "$1" = "read_param" ]; then
  printf "${CYAN}Only read param${CYAN}\n"
  if [ -d "$RPI_SCRIPTS" ]; then
    printf "$RPI_SCRIPTS/params.sh\n"
  fi
  if [ -d "$UTILS_SCRIPTS" ]; then
    printf "$UTILS_SCRIPTS/params.sh\n"
  fi
else
  source $UTILS_SCRIPTS/deploy-utils.sh $1
fi