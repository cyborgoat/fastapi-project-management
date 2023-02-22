#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   api.py
@Time    :   2023/02/22
@Author  :   Junxiao Guo
@Version :   1.0
@License :   (C)Copyright 2022-2023, Junxiao Guo
@Desc    :   None
'''
from fastapi import APIRouter
from app.api.api_v1.endpoints import projects

api_router = APIRouter()
api_router.include_router(projects.router, tags=['projects'])
