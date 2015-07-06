FROM frolvlad/alpine-python2 


RUN mkdir -p /app
ADD /BattlePyEngine /app
ADD /battlePyServer/upload /app/battlePy
WORKDIR /app


