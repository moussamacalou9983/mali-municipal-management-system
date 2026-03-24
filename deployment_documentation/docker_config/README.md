# docker-compose-laravel

Flux de travail Docker Compose simplifie qui met en place un reseau LEMP de conteneurs pour le developpement local Laravel. Vous pouvez consulter l'article complet qui a inspire ce depot [ici](https://dev.to/aschmelyun/the-beauty-of-docker-for-local-laravel-development-13c0).

## Utilisation

Pour commencer, assurez-vous que [Docker est installe](https://docs.docker.com/docker-for-mac/install/) sur votre systeme, puis clonez ce depot.

Ensuite, placez-vous dans le terminal dans le dossier clone et lancez les conteneurs du serveur web avec `docker-compose up -d --build site`.

Une fois cette etape terminee, suivez les instructions du fichier [src/README.md](src/README.md) pour ajouter votre projet Laravel ou en creer un nouveau vide.

Le demarrage du reseau Docker Compose avec `site` plutot qu'avec `up` seulement garantit que seuls les conteneurs de notre site sont demarres au debut, et non l'ensemble des conteneurs de commande. Les services suivants sont construits pour le serveur web, avec leurs ports exposes :

- **nginx** - `:80`
- **mysql** - `:3306`
- **php** - `:9000`
- **redis** - `:6379`
- **mailhog** - `:8025`

Trois conteneurs supplementaires sont egalement inclus pour executer les commandes Composer, NPM et Artisan *sans* avoir a installer ces plateformes sur votre ordinateur local. Utilisez les exemples ci-dessous depuis la racine du projet, en les adaptant a votre besoin.

- `docker-compose run --rm composer update`
- `docker-compose run --rm npm run dev`
- `docker-compose run --rm artisan migrate`

## Problemes de permissions

Si vous rencontrez des problemes de permissions sur le systeme de fichiers en accedant a l'application ou en executant une commande dans un conteneur, suivez l'un des jeux d'etapes ci-dessous.

**Si vous utilisez votre serveur ou environnement local en tant qu'utilisateur root :**

- Arretez les conteneurs avec `docker-compose down`
- Remplacez le fichier precedent par `docker-compose.root.yml`
- Reconstruisez les conteneurs avec `docker-compose build --no-cache`

**Si vous utilisez votre serveur ou environnement local avec un utilisateur non root :**

- Arretez les conteneurs avec `docker-compose down`
- Dans votre terminal, executez `export UID=$(id -u)` puis `export GID=$(id -g)`
- Si vous voyez des erreurs concernant des variables en lecture seule lors de l'etape precedente, vous pouvez les ignorer et continuer
- Reconstruisez les conteneurs avec `docker-compose build --no-cache`

Ensuite, redemarrez votre reseau de conteneurs ou relancez la commande que vous essayiez d'executer, puis verifiez si le probleme est resolu.

## Stockage MySQL persistant

Par defaut, lorsque vous arretez le reseau Docker, vos donnees MySQL sont supprimees apres destruction des conteneurs. Si vous souhaitez conserver des donnees persistantes apres arret puis redemarrage des conteneurs, procedez ainsi :

1. Creez un dossier `mysql` a la racine du projet, a cote des dossiers `nginx` et `src`.
2. Sous le service mysql dans votre fichier `docker-compose.yml`, ajoutez les lignes suivantes :

```yaml
volumes:
  - ./mysql:/var/lib/mysql
```

## Utiliser BrowserSync avec Laravel Mix

Si vous souhaitez activer le rechargement a chaud fourni par l'option BrowserSync de Laravel Mix, quelques etapes supplementaires sont necessaires. Commencez par verifier que vous utilisez le `docker-compose.yml` mis a jour avec les ports `:3000` et `:3001` ouverts sur le service npm. Ajoutez ensuite ce qui suit a la fin du fichier `webpack.mix.js` de votre projet Laravel :

```javascript
.browserSync({
    proxy: 'site',
    open: false,
    port: 3000,
});
```

Depuis le terminal a la racine du projet, executez la commande suivante pour surveiller les changements avec le conteneur npm et ses ports associes :

```bash
docker-compose run --rm --service-ports npm run watch
```

Cela laissera ouvert un petit panneau d'information dans votre terminal, que vous pouvez quitter avec `Ctrl + C`. En visitant [localhost:3000](http://localhost:3000) dans votre navigateur, vous devriez alors charger l'application Laravel avec BrowserSync active et le rechargement a chaud en fonctionnement.

## MailHog

La version actuelle de Laravel utilise MailHog comme application par defaut pour tester l'envoi d'emails et le fonctionnement SMTP general pendant le developpement local. Avec l'image Docker Hub fournie, sa mise en place est simple et directe. Le service est inclus dans le fichier `docker-compose.yml` et demarre en meme temps que le serveur web et la base de donnees.

Pour consulter le tableau de bord et visualiser les emails transitant par le systeme, rendez-vous sur [localhost:8025](http://localhost:8025) apres avoir execute `docker-compose up -d site`.
