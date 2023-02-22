#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   projects.py
@Time    :   2023/02/22
@Author  :   Junxiao Guo
@Version :   1.0
@License :   (C)Copyright 2022-2023, Junxiao Guo
@Desc    :   None
'''
from typing import List

from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=List[str])
def read_projects() -> List[str]:
    """Fetch Projects"""
    return ['proj1', 'proj2']
