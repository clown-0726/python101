import mmap

"""
mmap 也是零拷贝技术，直接将 IO 设备内容映射到内存地址的一种方式。
- 在访问某些二进制文件时，希望能把文件映射到内存中，可以实现随机访问。（比如 framebuffer 设备文件）
- 某些嵌入式设备，寄存器被编址到内存地址空间，我们可以映射 /dev/mem 某范围，去访问这些寄存器。
- 如果多个进程映射同一个文件，还能实现进程通信的目的。

在下面例子中，通过第一个命令创建一个文件作为测试文件，第二命令查看文件的内容
dd if=/dev/zero of=demo.bin bs=1024 count=1024
od -x demo.bin
"""

f = open("demo.bin", "rb+")
fd = f.fileno()

m = mmap.mmap(fileno=fd, length=0, access=mmap.ACCESS_WRITE)
print(m[0])
m[0] = b"\x88"[0]
m[1] = 0x88
print(m[0], m[1])
