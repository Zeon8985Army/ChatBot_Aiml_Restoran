# Jika Belum ada AIML
# pip install python-aiml
import aiml, os


# membuat kernel dan mempelajari berkas AIML
kernel = aiml.Kernel()

# Lebih cepat jika sudah ada Bootstrapping
if os.path.isfile("maleo_brain.brn"):
    kernel.bootstrap(brainFile = "maleo_brain.brn")
else:
    kernel.bootstrap(learnFiles = "start.xml", commands = "CAFE")
    kernel.saveBrain("maleo_brain.brn")

def get_respond_from_backend(msg):
    print(msg)
    if (kernel.respond(msg)):
        return (kernel.respond(msg))
    else:
        msg = msg+"ya"
        if (kernel.respond(msg)):
            return (kernel.respond(msg))
        else:
            msg = "ya "+msg+"ya"
            if (kernel.respond(msg)):
                return (kernel.respond(msg))
            else:
                return "Maaf... saya kurang mengerti"
