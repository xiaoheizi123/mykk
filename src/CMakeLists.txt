#所有的路径变量都不允许重名
AUX_SOURCE_DIRECTORY(. T1_SRC_LIST)
#设置成静态库
ADD_LIBRARY(kcf ${T1_SRC_LIST})

INCLUDE_DIRECTORIES(/usr/local/opencv-2.4.11/include)
LINK_DIRECTORIES(/usr/local/opencv-2.4.11/lib)
