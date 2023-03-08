import ctypes

# Definición manual de tipos de datos necesarios
DWORD = ctypes.c_ulong
LONG = ctypes.c_long
ULONG_PTR = ctypes.POINTER(DWORD)
MAX_PATH = 260

class PROCESSENTRY32(ctypes.Structure):
    _fields_ = [
        ("dwSize", DWORD),
        ("cntUsage", DWORD),
        ("th32ProcessID", DWORD),
        ("th32DefaultHeapID", ULONG_PTR),
        ("th32ModuleID", DWORD),
        ("cntThreads", DWORD),
        ("th32ParentProcessID", DWORD),
        ("pcPriClassBase", LONG),
        ("dwFlags", DWORD),
        ("szExeFile", ctypes.c_char * MAX_PATH)
    ]

def kill_process_by_name(process_name):
    """
    Terminates a process by its name using ctypes and kernel32.
    """

    PROCESS_TERMINATE = 1
    handle = ctypes.windll.kernel32.CreateToolhelp32Snapshot(ctypes.c_uint32(0x2), ctypes.c_uint32(0))
    entry = PROCESSENTRY32()
    entry.dwSize = ctypes.sizeof(entry)

    while ctypes.windll.kernel32.Process32Next(handle, ctypes.byref(entry)):
        if process_name.lower() == entry.szExeFile.decode('utf-8').lower():
            handle_process = ctypes.windll.kernel32.OpenProcess(PROCESS_TERMINATE, False, entry.th32ProcessID)
            ctypes.windll.kernel32.TerminateProcess(handle_process, 0)
            ctypes.windll.kernel32.CloseHandle(handle_process)
