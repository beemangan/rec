# coding: utf-8

"""
    Public Robot Events API

    An API to access data on Robot Events officially. ## Request Metadata Pagination is performed the same way throughout each pageable endpoint using the query parameters `page` and `per_page`. Please not that dates should be formatted according to RFC3339.   # noqa: E501

    The version of the OpenAPI document: 1.0.21
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from rec import schemas  # noqa: F401


class Season(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int32Schema
            name = schemas.StrSchema
        
            @staticmethod
            def program() -> typing.Type['IdInfo']:
                return IdInfo
            start = schemas.DateTimeSchema
            end = schemas.DateTimeSchema
            years_start = schemas.Int32Schema
            years_end = schemas.Int32Schema
            __annotations__ = {
                "id": id,
                "name": name,
                "program": program,
                "start": start,
                "end": end,
                "years_start": years_start,
                "years_end": years_end,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["program"]) -> 'IdInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["years_start"]) -> MetaOapg.properties.years_start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["years_end"]) -> MetaOapg.properties.years_end: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "program", "start", "end", "years_start", "years_end", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["program"]) -> typing.Union['IdInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> typing.Union[MetaOapg.properties.start, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end"]) -> typing.Union[MetaOapg.properties.end, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["years_start"]) -> typing.Union[MetaOapg.properties.years_start, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["years_end"]) -> typing.Union[MetaOapg.properties.years_end, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "program", "start", "end", "years_start", "years_end", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        program: typing.Union['IdInfo', schemas.Unset] = schemas.unset,
        start: typing.Union[MetaOapg.properties.start, str, datetime, schemas.Unset] = schemas.unset,
        end: typing.Union[MetaOapg.properties.end, str, datetime, schemas.Unset] = schemas.unset,
        years_start: typing.Union[MetaOapg.properties.years_start, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        years_end: typing.Union[MetaOapg.properties.years_end, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Season':
        return super().__new__(
            cls,
            *args,
            id=id,
            name=name,
            program=program,
            start=start,
            end=end,
            years_start=years_start,
            years_end=years_end,
            _configuration=_configuration,
            **kwargs,
        )

from rec.model.id_info import IdInfo
