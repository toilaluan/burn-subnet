import bittensor as bt
import argparse
import time


parser = argparse.ArgumentParser(description="Bittensor Burn Subnet CLI")

parser.add_argument(
    "--netuid",
    type=int,
    default=47,
)
parser.add_argument(
    "--wallet-name",
    type=str,
    default="default",
)

parser.add_argument(
    "--wallet-hotkey",
    type=str,
    default="default",
)

parser.add_argument(
    "--burn-uid",
    type=int,
    default=245,
)

args = parser.parse_args()

print("Initializing Subtensor...")
SUBTENSOR = bt.subtensor()
METAGRAPH = bt.metagraph(args.netuid)
WALLET = bt.wallet(
    name=args.wallet_name,
    hotkey=args.wallet_hotkey,
)

print("Subtensor initialized.")
print("Wallet initialized.")
print("Metagraph initialized.")

while True:
    print("Burning Subnet Uid: ", args.burn_uid, " at ", time.time())
    uids = [args.burn_uid]
    weights = [1.0]
    try:
        result = SUBTENSOR.set_weights(
            wallet=WALLET,
            uids=uids,
            weights=weights,
            netuid=args.netuid,
            version_key=10,
        )
        print("Result: ", result)
    except Exception as e:
        print("Error: ", e)

    time.sleep(600)

    