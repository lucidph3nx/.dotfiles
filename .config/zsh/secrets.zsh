## load secrets from sops
export SOPS_AGE_KEY_FILE="$XDG_CONFIG_HOME/sops/age/keys.txt"
SECRETS_FILE="$XDG_CONFIG_HOME/secrets/encrypted.sops"
# decrypt secrets if age key is present
if [[ -f $SOPS_AGE_KEY_FILE ]] && [[ -f $SECRETS_FILE ]]; then
  eval "$(sops --decrypt $SECRETS_FILE)"
else
  echo "Warning: Age key not found or secrets file not present. Skipping secrets decryption."
fi

# os specific secrets
if [[ "$OSTYPE" == "darwin"* ]]; then
  export BW_SESSION="$BW_SESSION_MAC"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
  export BW_SESSION="$BW_SESSION_NAV"
fi
export BW_SESSION_MAC=""
export BW_SESSION_NAV=""

