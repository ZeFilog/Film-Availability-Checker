# scrap_film
Bien sûr! Voici un résumé détaillé du fonctionnement du projet et de chaque fonction :

Le projet "Film Availability Checker" est un programme Python qui permet de rechercher la disponibilité des films sur les plateformes de streaming comme Amazon Prime Video, Netflix et Disney+. Voici comment le programme fonctionne :

1. **search_google(query):** Cette fonction utilise la bibliothèque Selenium pour effectuer une recherche Google avec la requête spécifiée. Elle ouvre une instance du navigateur Chrome, accède à la page de résultats de recherche Google et récupère le code HTML de la page. Elle retourne ensuite le code HTML.

2. **extract_div_elements(html, class_names):** Cette fonction utilise la bibliothèque BeautifulSoup pour extraire les éléments `<div>` du code HTML qui correspondent aux résultats de recherche des films. Elle parcourt les éléments `<div>` en utilisant les noms de classe spécifiés et extrait le titre et la description de chaque résultat. Les résultats sont stockés dans un dictionnaire où le titre est la clé et la description est la valeur. La fonction retourne ce dictionnaire.

3. **filter_results(results):** Cette fonction filtre les résultats de recherche en ne gardant que les résultats qui correspondent aux plateformes de streaming spécifiées et qui sont disponibles en abonnement. Elle parcourt le dictionnaire de résultats et vérifie si la clé (la plateforme) se trouve parmi les plateformes souhaitées (Amazon Prime Video, Netflix et Disney+) et si la valeur (la description) indique un abonnement. Les résultats filtrés sont stockés dans un nouveau dictionnaire et retournés.

4. **read_movie_names(file_path):** Cette fonction lit les noms des films à partir d'un fichier texte spécifié. Elle ouvre le fichier, lit chaque ligne (qui correspond à un nom de film) et les ajoute à une liste. La liste de noms de films est ensuite retournée.

5. **add_movie_names(file_path):** Cette fonction permet à l'utilisateur d'ajouter des noms de films au fichier texte spécifié. Elle utilise une boucle while qui demande à l'utilisateur d'entrer le nom d'un film à ajouter. Si l'utilisateur entre 'q', la boucle se termine. Sinon, le nom du film est ajouté à la fin du fichier texte.

6. **remove_movie_names(file_path):** Cette fonction permet à l'utilisateur de supprimer des noms de films du fichier texte spécifié. Elle lit d'abord tous les noms de films à partir du fichier, puis affiche la liste des films disponibles avec un numéro associé. L'utilisateur est invité à entrer le numéro du film à supprimer. Si l'utilisateur entre 0, la boucle se termine. Sinon, le film correspondant au numéro est supprimé de la liste et la liste mise à jour est réécrite dans le fichier.

Ensuite, le programme principal s'exécute :

1. Il lit les noms des films à partir du fichier texte.

2. Il permet à l'utilisateur d'ajouter ou de supprimer des noms de films.

3. Il lit à nouveau les noms de films mis à jour à partir du fichier.

4. Pour chaque nom de film, il effectue une recherche Google en utilisant la fonction `search_google()` et récupère les résultats de recherche.

5. Il extrait les résultats pertinents en utilisant la fonction `extract_div_elements()` et les filtre en utilisant la fonction `filter_results()`.

6.

 Enfin, il affiche les informations de disponibilité des films sur les différentes plateformes.

Cela permet à l'utilisateur de vérifier facilement la disponibilité des films sur les plateformes de streaming populaires.

J'espère que cela vous aide à comprendre le fonctionnement du projet. Si vous avez d'autres questions, n'hésitez pas à demander !
