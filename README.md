# ARECE Trajectory

## Contrôle d'un véhicule simulé avec une manette de PS4

### Premier pas
Pour prendre en main ROS2 il a été mis en place cette petite interface graphique. Cette application sert à comprendre le fonctionnement des noeuds ROS.
Nous avons ici 2 Noeuds le premier est un service qui va recevoir 2 entiers d'un client puis lui retourner la somme de ces 2 entiers.
Le deuxième noeud est une interface graphique qui va permettre à l'utilisateur de rentrer 2 entiers, et, qui après avoir envoyé ces 2 entiers à l'autre noeuds récupère la somme et affiche le calcul en console.

### Installation

1. [Installer ROS](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)
2. Installer les packages python nécessaire
3. Installer l'application

#### Installation automatique
Installer tous les packages en éxecutant le fichier `installPackages.sh`

```bash
./installPackages.sh
```
#### Installation manuelle
Commencer par installer la bibliothèque `evdev` qui permet de gérer les entrées et sorties des périphériques en python.

```bash
pip install evdev
```

Pour installer l'aplication aller à la racine du dossier.

Installer les différentes dépendances :

```bash
rosdep install -i --from-path src --rosdistro humble -y
```

Compiler l'application :
```bash
colcon build --packages-select py_manette_ps4
```

Enfin finir l'installation :
```bash
source install/setup.bash
```
En cas d'utilisation de `zsh` remplacer `setup.bash` par `setup.zsh`

Vous devriez maintenant avoir en plus du dossier `src` trois nouveaux dossiers : `build`, `install`, et `log`

### fonctionnement 

Maintenant que l'installation est faite, vous pouvez lancer l'application.

Dans un premier temps lancer le service :
```bash
ros2 run py_manette_ps4 talker
```
Ouvrez un nouveau terminal et lancer le client
```bash
ros2 run py_manette_ps4 listener
```


