import warnings

def pytest_configure(config):
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="google._upb._message")
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="google._upb._message.MessageMapContainer")
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="google._upb._message.ScalarMapContainer")
