import sys


def wait_for_enter():
    input("Press Enter to continue: ")


class CreateSSHKeypairStep(object):

    def run(self, context):
        print("Run:")
        print("   ssh-keygen -t rsa -f ~/{0}".format(context["username"]))
        wait_for_enter()


class GitCommitStep(object):

    def run(self, text):
        print("Copy ~/new_key.pub into `user_keys` Git repository -> run:")
        print("    git commit {0}".format(context["username"]))
        print("    git push")
        wait_for_enter()


class WaitForBuildStep(object):
    build_url = "http://orange.com/builds/user_keys"

    def run(self, text):
        print("Wait for the build job at {0} to finish".format(self.build_url))
        wait_for_enter()


class RetrieveUserEmailStep(object):
    dir_url = "http://orange.com/directory"

    def run(self, text):
        print("Go to {0}".format(self.dir_url))
        print("Find the email address for user `{0}`".format(context["username"]))
        context["email"] = input("add the email address and press enter: ")


class SendPrivateKeyStep(object):
    def run(self, text):
        print("Go to Password")
        print("add the contents of ~/new_key into a new document")
        print("share the document with {0}".format(context["email"]))
        wait_for_enter()


if __name__ == "__main__":
    context = {"username": sys.argv[0]}
    procedure = [
        CreateSSHKeypairStep(),
        GitCommitStep(),
        WaitForBuildStep(),

        RetrieveUserEmailStep(),
        SendPrivateKeyStep(),
    ]
    for step in procedure:
        step.run(context)
    print("Done.")
