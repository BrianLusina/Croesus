import os


def setup_environment_variables():
    """
    import environment variables    
    :return: 
    """
    if os.path.exists(".env"):
        print("Importing environment variables")
        for line in open(".env"):
            var = line.strip().split("=")
            if len(var) == 2:
                os.environ[var[0]] = var[1]
<<<<<<< HEAD

if __name__ == "__main__":
    setup_environment_variables()
=======
>>>>>>> remove log rocket dependency
