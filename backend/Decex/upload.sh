username="apple"
boxip="208.109.12.145"
sourcedir="/Users/rongbaizhang/PycharmProjects/DecexDiploy/Decex/backend/Decex"
rsync -t -a -v -z --exclude=".idea" --exclude=".git" --exclude="tests" --exclude="*.hdf5" --exclude="runtime/*" ${sourcedir} -e "ssh " ${username}@${boxip}:/home/apple/PythonProjects

