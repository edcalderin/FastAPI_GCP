
    # Fast API with GCP

    ## Use this configuration in launch.json
    
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "src.app:app"
            ],
            "console": "integratedTerminal"
        }
    ]
}