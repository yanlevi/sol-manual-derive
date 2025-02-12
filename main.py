from sol import xpub_to_address

fpub = "your_fpub"
last_vault_id = 0
run_until = last_vault_id + 1000000

for i in range(last_vault_id, run_until):
    print(f"Vault ID: {i}, Address: {xpub_to_address(fpub, i)}")
