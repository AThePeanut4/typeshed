"""
Provides an ``ndb`` interface for the blob store.

Initially, the blob store was an App Engine specific API for Google Cloud
Storage.

No longer supported.
"""

from typing import Any

from google.cloud.ndb import model

BlobKey: Any
BLOB_INFO_KIND: str
BLOB_MIGRATION_KIND: str
BLOB_KEY_HEADER: str
BLOB_RANGE_HEADER: str
MAX_BLOB_FETCH_SIZE: int
UPLOAD_INFO_CREATION_HEADER: str
BlobKeyProperty = model.BlobKeyProperty

class BlobFetchSizeTooLargeError:
    def __init__(self, *args, **kwargs) -> None: ...

class BlobInfo:
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def get(cls, *args, **kwargs) -> None: ...
    @classmethod
    def get_async(cls, *args, **kwargs) -> None: ...
    @classmethod
    def get_multi(cls, *args, **kwargs) -> None: ...
    @classmethod
    def get_multi_async(cls, *args, **kwargs) -> None: ...

class BlobInfoParseError:
    def __init__(self, *args, **kwargs) -> None: ...

class BlobNotFoundError:
    def __init__(self, *args, **kwargs) -> None: ...

class BlobReader:
    def __init__(self, *args, **kwargs) -> None: ...

def create_upload_url(*args, **kwargs) -> None: ...
def create_upload_url_async(*args, **kwargs) -> None: ...

class DataIndexOutOfRangeError:
    def __init__(self, *args, **kwargs) -> None: ...

def delete(*args, **kwargs) -> None: ...
def delete_async(*args, **kwargs) -> None: ...
def delete_multi(*args, **kwargs) -> None: ...
def delete_multi_async(*args, **kwargs) -> None: ...

class Error:
    def __init__(self, *args, **kwargs) -> None: ...

def fetch_data(*args, **kwargs) -> None: ...
def fetch_data_async(*args, **kwargs) -> None: ...

get: Any
get_async: Any
get_multi: Any
get_multi_async: Any

class InternalError:
    def __init__(self, *args, **kwargs) -> None: ...

def parse_blob_info(*args, **kwargs) -> None: ...

class PermissionDeniedError:
    def __init__(self, *args, **kwargs) -> None: ...
