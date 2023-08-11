from metaclass_singleton import FileSingleton

logger1 = FileSingleton()
logger1.set_file_address("./teste.txt")
logger1.print_address()
logger2 = FileSingleton()
logger1.print_address()

print(logger1, logger2)