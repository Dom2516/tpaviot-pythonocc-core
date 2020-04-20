from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopAbs import *


class TopBas_ListOfTestInterference:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> TopBas_TestInterference: ...
    def Last(self) -> TopBas_TestInterference: ...
    def Append(self, theItem: TopBas_TestInterference) -> TopBas_TestInterference: ...
    def Prepend(self, theItem: TopBas_TestInterference) -> TopBas_TestInterference: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> TopBas_TestInterference: ...
    def SetValue(self, theIndex: int, theValue: TopBas_TestInterference) -> None: ...

class TopBas_TestInterference:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Inters: float, Bound: int, Orient: TopAbs_Orientation, Trans: TopAbs_Orientation, BTrans: TopAbs_Orientation) -> None: ...
	@overload
	def Boundary(self, B: int) -> None: ...
	@overload
	def Boundary(self) -> int: ...
	@overload
	def BoundaryTransition(self, BTr: TopAbs_Orientation) -> None: ...
	@overload
	def BoundaryTransition(self) -> TopAbs_Orientation: ...
	def GetChangeBoundary(self) -> int: ...
	def SetChangeBoundary(self, value: int) -> None: ...
	def GetChangeIntersection(self) -> float: ...
	def SetChangeIntersection(self, value: float) -> None: ...
	@overload
	def Intersection(self, I: float) -> None: ...
	@overload
	def Intersection(self) -> float: ...
	@overload
	def Orientation(self, O: TopAbs_Orientation) -> None: ...
	@overload
	def Orientation(self) -> TopAbs_Orientation: ...
	@overload
	def Transition(self, Tr: TopAbs_Orientation) -> None: ...
	@overload
	def Transition(self) -> TopAbs_Orientation: ...

# harray1 classes
# harray2 classes
# hsequence classes

