Reinitaliser la BDD via:
```shell
	python3 models.py
```

Demarrer le serveur local(125.0.0.1:5000) avec:
```shell
	python3 app.py
```

.Exemple de requete pour creer/modifier une tache

```shell
{
    "task":{
        "t_id": 1,
        "t_title": "tache_test",
        "t_description": "description_test",
        "t_done": false
    }
}
```
