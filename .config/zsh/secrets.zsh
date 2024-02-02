## load secrets from sops
export SOPS_AGE_KEY_FILE="$XDG_CONFIG_HOME/sops/age/keys.txt"
SECRETS_FILE="$XDG_CONFIG_HOME/secrets/encrypted.sops"
# decrypt secrets if age key is present
if [[ -f $SOPS_AGE_KEY_FILE ]] && [[ -f $SECRETS_FILE ]]; then
  eval "$(sops --decrypt $SECRETS_FILE)"
  # set bw session on mac because it isnt done at os level
#   if [[ "$OSTYPE" == "darwin"* ]]; then
#     export BW_SESSION=$(bw unlock --raw $BW_KEY 2>/dev/null)
#   fi
else
  echo "Warning: Age key not found or secrets file not present. Skipping secrets decryption."
fi

