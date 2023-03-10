from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BRepAdaptor import *
from OCC.Core.GeomAbs import *
from OCC.Core.gp import *


class breplprop:
    @overload
    @staticmethod
    def Continuity(C1: BRepAdaptor_Curve, C2: BRepAdaptor_Curve, u1: float, u2: float, tl: float, ta: float) -> GeomAbs_Shape: ...
    @overload
    @staticmethod
    def Continuity(C1: BRepAdaptor_Curve, C2: BRepAdaptor_Curve, u1: float, u2: float) -> GeomAbs_Shape: ...

class BRepLProp_CLProps:
    @overload
    def __init__(self, C: BRepAdaptor_Curve, N: int, Resolution: float) -> None: ...
    @overload
    def __init__(self, C: BRepAdaptor_Curve, U: float, N: int, Resolution: float) -> None: ...
    @overload
    def __init__(self, N: int, Resolution: float) -> None: ...
    def CentreOfCurvature(self, P: gp_Pnt) -> None: ...
    def Curvature(self) -> float: ...
    def D1(self) -> gp_Vec: ...
    def D2(self) -> gp_Vec: ...
    def D3(self) -> gp_Vec: ...
    def IsTangentDefined(self) -> bool: ...
    def Normal(self, N: gp_Dir) -> None: ...
    def SetCurve(self, C: BRepAdaptor_Curve) -> None: ...
    def SetParameter(self, U: float) -> None: ...
    def Tangent(self, D: gp_Dir) -> None: ...
    def Value(self) -> gp_Pnt: ...

class BRepLProp_CurveTool:
    @staticmethod
    def Continuity(C: BRepAdaptor_Curve) -> int: ...
    @staticmethod
    def D1(C: BRepAdaptor_Curve, U: float, P: gp_Pnt, V1: gp_Vec) -> None: ...
    @staticmethod
    def D2(C: BRepAdaptor_Curve, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
    @staticmethod
    def D3(C: BRepAdaptor_Curve, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
    @staticmethod
    def FirstParameter(C: BRepAdaptor_Curve) -> float: ...
    @staticmethod
    def LastParameter(C: BRepAdaptor_Curve) -> float: ...
    @staticmethod
    def Value(C: BRepAdaptor_Curve, U: float, P: gp_Pnt) -> None: ...

class BRepLProp_SLProps:
    @overload
    def __init__(self, S: BRepAdaptor_Surface, U: float, V: float, N: int, Resolution: float) -> None: ...
    @overload
    def __init__(self, S: BRepAdaptor_Surface, N: int, Resolution: float) -> None: ...
    @overload
    def __init__(self, N: int, Resolution: float) -> None: ...
    def CurvatureDirections(self, MaxD: gp_Dir, MinD: gp_Dir) -> None: ...
    def D1U(self) -> gp_Vec: ...
    def D1V(self) -> gp_Vec: ...
    def D2U(self) -> gp_Vec: ...
    def D2V(self) -> gp_Vec: ...
    def DUV(self) -> gp_Vec: ...
    def GaussianCurvature(self) -> float: ...
    def IsCurvatureDefined(self) -> bool: ...
    def IsNormalDefined(self) -> bool: ...
    def IsTangentUDefined(self) -> bool: ...
    def IsTangentVDefined(self) -> bool: ...
    def IsUmbilic(self) -> bool: ...
    def MaxCurvature(self) -> float: ...
    def MeanCurvature(self) -> float: ...
    def MinCurvature(self) -> float: ...
    def Normal(self) -> gp_Dir: ...
    def SetParameters(self, U: float, V: float) -> None: ...
    def SetSurface(self, S: BRepAdaptor_Surface) -> None: ...
    def TangentU(self, D: gp_Dir) -> None: ...
    def TangentV(self, D: gp_Dir) -> None: ...
    def Value(self) -> gp_Pnt: ...

class BRepLProp_SurfaceTool:
    @staticmethod
    def Bounds(S: BRepAdaptor_Surface) -> Tuple[float, float, float, float]: ...
    @staticmethod
    def Continuity(S: BRepAdaptor_Surface) -> int: ...
    @staticmethod
    def D1(S: BRepAdaptor_Surface, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec) -> None: ...
    @staticmethod
    def D2(S: BRepAdaptor_Surface, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, DUV: gp_Vec) -> None: ...
    @staticmethod
    def DN(S: BRepAdaptor_Surface, U: float, V: float, IU: int, IV: int) -> gp_Vec: ...
    @staticmethod
    def Value(S: BRepAdaptor_Surface, U: float, V: float, P: gp_Pnt) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

breplprop_Continuity = breplprop.Continuity
breplprop_Continuity = breplprop.Continuity
BRepLProp_CurveTool_Continuity = BRepLProp_CurveTool.Continuity
BRepLProp_CurveTool_D1 = BRepLProp_CurveTool.D1
BRepLProp_CurveTool_D2 = BRepLProp_CurveTool.D2
BRepLProp_CurveTool_D3 = BRepLProp_CurveTool.D3
BRepLProp_CurveTool_FirstParameter = BRepLProp_CurveTool.FirstParameter
BRepLProp_CurveTool_LastParameter = BRepLProp_CurveTool.LastParameter
BRepLProp_CurveTool_Value = BRepLProp_CurveTool.Value
BRepLProp_SurfaceTool_Bounds = BRepLProp_SurfaceTool.Bounds
BRepLProp_SurfaceTool_Continuity = BRepLProp_SurfaceTool.Continuity
BRepLProp_SurfaceTool_D1 = BRepLProp_SurfaceTool.D1
BRepLProp_SurfaceTool_D2 = BRepLProp_SurfaceTool.D2
BRepLProp_SurfaceTool_DN = BRepLProp_SurfaceTool.DN
BRepLProp_SurfaceTool_Value = BRepLProp_SurfaceTool.Value
