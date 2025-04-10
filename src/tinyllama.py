import subprocess
import time
import psutil

def run_tinyllama(prompt):
    process = psutil.Process()
    start_time = time.time()
    cpu_percent_start = psutil.cpu_percent(interval=None)  # Initial CPU usage reading
    memory_usage_start = process.memory_info().rss
    try:
        # Run the ollama command with TinyLlama
        result = subprocess.run(
            ['ollama', 'run', 'tinyllama'],
            input=prompt.encode('utf-8'),
            capture_output=True,
            check=True
        )
        # Output from TinyLlama
        response = result.stdout.decode('utf-8')
        end_time = time.time()

        cpu_percent_end = psutil.cpu_percent(interval=None)  # Final CPU usage reading
        memory_usage_end = process.memory_info().rss

        print(f"\nCPU Usage: {cpu_percent_end:.2f}%")
        print(f"Memory Usage: {memory_usage_end - memory_usage_start} bytes")
        print(f"Elapsed time: {end_time - start_time:.2f} seconds")
        return response.strip()
    except subprocess.CalledProcessError as e:
        print("Error running TinyLlama:", e.stderr.decode('utf-8'))
        return None
    
def run_mistral(prompt):
    process = psutil.Process()
    start_time = time.time()
    cpu_percent_start = psutil.cpu_percent(interval=None)  # Initial CPU usage reading
    memory_usage_start = process.memory_info().rss
    try:
        # Run the ollama command with TinyLlama
        result = subprocess.run(
            ['ollama', 'run', 'mistral'],
            input=prompt.encode('utf-8'),
            capture_output=True,
            check=True
        )
        # Output from TinyLlama
        response = result.stdout.decode('utf-8')
        end_time = time.time()

        cpu_percent_end = psutil.cpu_percent(interval=None)  # Final CPU usage reading
        memory_usage_end = process.memory_info().rss

        print(f"\nCPU Usage: {cpu_percent_end:.2f}%")
        print(f"Memory Usage: {memory_usage_end - memory_usage_start} bytes")
        print(f"Elapsed time: {end_time - start_time:.2f} seconds")
        return response.strip()
    except subprocess.CalledProcessError as e:
        print("Error running Mistral:", e.stderr.decode('utf-8'))
        return None
    
def run_llama2(prompt):
    process = psutil.Process()
    start_time = time.time()
    cpu_percent_start = psutil.cpu_percent(interval=None)  # Initial CPU usage reading
    memory_usage_start = process.memory_info().rss
    try:
        # Run the ollama command with TinyLlama
        result = subprocess.run(
            ['ollama', 'run', 'llama2'],
            input=prompt.encode('utf-8'),
            capture_output=True,
            check=True
        )
        # Output from TinyLlama
        response = result.stdout.decode('utf-8')
        end_time = time.time()

        cpu_percent_end = psutil.cpu_percent(interval=None)  # Final CPU usage reading
        memory_usage_end = process.memory_info().rss

        print(f"\nCPU Usage: {cpu_percent_end:.2f}%")
        print(f"Memory Usage: {memory_usage_end - memory_usage_start} bytes")
        print(f"Elapsed time: {end_time - start_time:.2f} seconds")
        return response.strip()
    except subprocess.CalledProcessError as e:
        print("Error running Llama2:", e.stderr.decode('utf-8'))
        return None

if __name__ == "__main__":
    prompts = {"What is the height of the Eiffel Tower?",
               "Do any countries own Antarctica?",
               """Summarize the following text:
                Cameroon,[a] officially the Republic of Cameroon,[b] is a country in Central Africa. It shares boundaries with Nigeria to the west and north, Chad to the northeast, the Central African Republic to the east, and Equatorial Guinea, Gabon, and the Republic of the Congo to the south. Its coastline lies on the Bight of Biafra, part of the Gulf of Guinea, and the Atlantic Ocean. Due to its strategic position at the crossroads between West Africa and Central Africa, it has been categorized as being in both camps. Cameroon's population of nearly 31 million people speak 250 native languages, in addition to the national tongues of English and French, or both. Early inhabitants of the territory included the Sao civilisation around Lake Chad and the Baka hunter-gatherers in the southeastern rainforest. Portuguese explorers reached the coast in the 15th century and named the area Rio dos Camarões (Shrimp River), which became Cameroon in English. Fulani soldiers founded the Adamawa Emirate in the north in the 19th century, and various ethnic groups of the west and northwest established powerful chiefdoms and fondoms.
                """,
                "Write a Python script to check if an integer is prime.",
                "Write a short story about a squirrel on an adventure."}
    #Iterate through each prompt for each model
    print("\nTinyLlama Testing:\n")
    for prompt in prompts:
        print("Prompt: ", prompt)
        response = run_tinyllama(prompt)
        if response:
            print("\nResponse:")
            print(response)
    print("\nMistral Testing:\n")
    for prompt in prompts:
        print("Prompt: ", prompt)
        response = run_mistral(prompt)
        if response:
            print("\nResponse:")
            print(response)
    print("\nLlama2 Testing:\n")
    for prompt in prompts:
        print("Prompt: ", prompt)
        response = run_llama2(prompt)
        if response:
            print("\nResponse:")
            print(response)
