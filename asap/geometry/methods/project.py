from OCC import GeomProjLib
from OCC.GeomAPI import GeomAPI_ProjectPointOnCurve, GeomAPI_ProjectPointOnSurf
from OCC.GeomAbs import GeomAbs_BSplineCurve, GeomAbs_BezierCurve, GeomAbs_Line
from OCC.GeomAdaptor import GeomAdaptor_Curve

from .create import create_line_from_occ, create_nurbs_curve_from_occ


def project_point_to_curve(point, curve):
    """
    Project a point to a curve.
    """
    # OCC projection.
    proj = GeomAPI_ProjectPointOnCurve(point, curve.handle)

    # Gather results.
    npts = proj.NbPoints()
    results = []
    for i in range(1, npts + 1):
        u = proj.Parameter(i)
        d = proj.Distance(i)
        p = curve.eval(u)
        results.append([p, u, d])

    # Sort by distance and return.
    results.sort(key=lambda lst: lst[2])
    return results


def project_point_to_surface(point, surface):
    """
    Project a point to a surface.
    """
    # OCC projection.
    proj = GeomAPI_ProjectPointOnSurf(point, surface.handle)

    # Gather results.
    npts = proj.NbPoints()
    results = []
    for i in range(1, npts + 1):
        u, v = proj.Parameters(i)
        d = proj.Distance(i)
        p = surface.eval(u, v)
        results.append([p, (u, v), d])

    # Sort by distance and return.
    results.sort(key=lambda lst: lst[2])
    return results


def project_curve_to_plane(curve, plane, v, keep_param=True):
    """
    Project a curve to a plane along the vector.
    """
    # OCC projection.
    hcrv = GeomProjLib.geomprojlib_ProjectOnPlane(curve.handle, plane.handle,
                                                  v, keep_param)
    if hcrv.IsNull():
        return None

    # Convert.
    adp_crv = GeomAdaptor_Curve(hcrv)
    if adp_crv.GetType() == GeomAbs_Line:
        lin = create_line_from_occ(adp_crv.Line())
        return create_line_from_occ(lin)

    if adp_crv.GetType() in [GeomAbs_BezierCurve, GeomAbs_BSplineCurve]:
        crv = adp_crv.BSpline().GetObject()
        return create_nurbs_curve_from_occ(crv)

    return None


def project_curve_to_surface(curve, surface):
    """
    Project a curve to a surface.
    """
    # OCC projection. Catch error in case curve is outside the surface
    # boundaries.
    try:
        hcrv = GeomProjLib.geomprojlib_Project(curve.handle, surface.handle)
        if hcrv.IsNull():
            return None
    except RuntimeError:
        return None

    # Convert.
    adp_crv = GeomAdaptor_Curve(hcrv)
    if adp_crv.GetType() == GeomAbs_Line:
        lin = create_line_from_occ(adp_crv.Line())
        return create_line_from_occ(lin)

    if adp_crv.GetType() in [GeomAbs_BezierCurve, GeomAbs_BSplineCurve]:
        crv = adp_crv.BSpline().GetObject()
        return create_nurbs_curve_from_occ(crv)

    return None