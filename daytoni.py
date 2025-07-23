from daytona import Daytona, DaytonaConfig
  
# Define the configuration
config = DaytonaConfig(api_key="dtn_65c10bd3da5ba392171806def2b21f0ad1013852708ff74c3566f34f9764bd41")

# Initialize the Daytona client
daytona = Daytona(config)

# Create the Sandbox instance
sandbox = daytona.create()
resources=Resources(
        cpu=4,         # 4 vCPUs
        memory=8,      # 8 GiB RAM
        disk=16        # 16 GiB disk
    )

# Run the code securely inside the Sandbox
response = sandbox.process.code_run('print("Hello World from code!")')
if response.exit_code != 0:
  print(f"Error: {response.exit_code} {response.result}")
else:
    print(response.result)
  
