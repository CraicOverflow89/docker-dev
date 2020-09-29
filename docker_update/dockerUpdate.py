import os, re


class DockerUpdate:
    @staticmethod
    def update():
        """
        Updates all of the repositories listed in the docker-compose file.
        :return: None
        """
        try:
            with open(f"{os.getcwd()}/../docker-compose.yml") as file:
                for line in file:
                    context = re.search("context: ([A-Za-z0-9.\-/]*)", line)
                    if context is not None:
                        DockerUpdate._update_repo(context.group(1))
            print("Completed")
        except FileNotFoundError:
            print(f"Could not locate the docker-compose file.")

    @staticmethod
    def _update_repo(path):
        """
        Updates a repository to latest version of the develop branch.
        :param path: the path to the repository
        :return: None
        """
        print(f"Updating {path[2:]}")
        os.system(f"cd ../{path} && git checkout develop && git pull")
        print("")
