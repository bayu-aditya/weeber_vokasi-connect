from envbash import load_envbash

load_envbash("secret/development.env")

if __name__ == "__main__":
  from main import app
  app.run(host="0.0.0.0", debug=True)