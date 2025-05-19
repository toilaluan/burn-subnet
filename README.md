## Burn Subnet Alpha

1. Install pm2, uv:
```bash
apt update && apt upgrade -y && apt-get install -y nano git python3-pip jq npm && npm install pm2 -g && pm2 update
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
```

2. Clone the repo:
```bash
git clone https://github.com/toilaluan/burn-subnet
cd burn-subnet
uv venv
. .venv/bin/activate
uv sync
```

3. Start burning:
```bash
pm2 start --name "burn-47" python -- -m main --wallet-name default --wallet-hotkey default --netuid 47 --burn-uid 245
```

