def get_config():
    config = {
        'project_id': input("Inserisci l'ID del progetto GCP: "),
        'topic_id': input("Inserisci l'ID del topic Pub/Sub: "),
        'subscription_id': input("Inserisci l'ID della sottoscrizione Pub/Sub: ")
    }
    return config
