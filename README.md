# Drone Engineering Ecosystem
![software-arch](https://user-images.githubusercontent.com/32190349/155320787-f8549148-3c93-448b-b79a-388623ca5d3f.png)

## Demo
[Drone Engineering Ecosystem demo](https://www.youtube.com/playlist?list=PL64O0POFYjHpXyP-T063RdKRJXuhqgaXY)

## Gate
The Gate module is responsible for interconnecting the local broker with the global broker,so it is really
interconnecting the software-on-board with the global broker.

## PreCommit
`pre-commit` is a pretty nice tool that allow us to run different actions in our code before we commit any file.
We will use it for formatting our code, "prettify" json files, etc. To install pre-commit on our code,
which will allow us to NOT commit the files if there is something wrong with them, we have to type on the top directory:

`pre-commit install`

If the pre-commit gets a little annoying, and you just want to commit files, you can deactivate it:

`pre-commit uninstall`

If we want to make sure that we can commit the files, and if not, why, then we need to run the following command:

`pre-commit run --all-files` or `pre-commit run -a`

By doing so, we ensure that, before uploading any file to GitHub, our code is well assembled.


## Example and tutorials

The basics of MQTT can be found here:
[MQTT](https://www.youtube.com/watch?v=EIxdz-2rhLs)

This is a good example to start using MQTT (using a public broker):
[Example](https://www.youtube.com/watch?v=kuyCd53AOtg)
