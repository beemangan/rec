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


class Alliance(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "score",
            "color",
            "teams",
        }
        
        class properties:
            
            
            class color(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def RED(cls):
                    return cls("red")
                
                @schemas.classproperty
                def BLUE(cls):
                    return cls("blue")
            score = schemas.Int32Schema
            
            
            class teams(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AllianceTeam']:
                        return AllianceTeam
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AllianceTeam'], typing.List['AllianceTeam']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'teams':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AllianceTeam':
                    return super().__getitem__(i)
            __annotations__ = {
                "color": color,
                "score": score,
                "teams": teams,
            }
    
    score: MetaOapg.properties.score
    color: MetaOapg.properties.color
    teams: MetaOapg.properties.teams
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["score"]) -> MetaOapg.properties.score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["teams"]) -> MetaOapg.properties.teams: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["color", "score", "teams", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["score"]) -> MetaOapg.properties.score: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["teams"]) -> MetaOapg.properties.teams: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["color", "score", "teams", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        score: typing.Union[MetaOapg.properties.score, decimal.Decimal, int, ],
        color: typing.Union[MetaOapg.properties.color, str, ],
        teams: typing.Union[MetaOapg.properties.teams, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Alliance':
        return super().__new__(
            cls,
            *args,
            score=score,
            color=color,
            teams=teams,
            _configuration=_configuration,
            **kwargs,
        )

from rec.model.alliance_team import AllianceTeam
