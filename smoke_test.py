import time

from hindsight_setup import get_client

client = get_client()

retain_result = client.retain(bank_id="test-bank", content="Testing connection")
print("RETAIN RESULT:", retain_result)

print("Waiting 20s for indexing...")
time.sleep(20)

reflect_result = client.reflect(bank_id="test-bank", query="What was tested?")
print("REFLECT RESULT:", reflect_result)