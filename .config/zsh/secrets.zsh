## load secrets from sops
export SOPS_AGE_KEY_FILE="$XDG_CONFIG_HOME/sops/age/age/keys.txt"
SECRETS_FILE="$XDG_CONFIG_HOME/secrets/encrypted.sops"
# decrypt secrets if age key is present
if [[ -f $SOPS_AGE_KEY_FILE ]] && [[ -f $SECRETS_FILE ]]; then
  eval "$(sops --decrypt $SECRETS_FILE)"
else
  echo "Warning: Age key not found or secrets file not present. Skipping secrets decryption."
fi

