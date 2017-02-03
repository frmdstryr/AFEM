from .methods.create_parts import create_bulkhead_by_sref, \
    create_floor_by_sref, create_frame_by_sref, create_surface_part, \
    create_wing_part_by_params, create_wing_part_by_points


class CreateSpar(object):
    """
    Spar creator.
    """

    @staticmethod
    def by_parameters(name, wing, u1, v1, u2, v2, rshape=None, build=True):
        """
        Create a spar by wing parameters.

        :param name:
        :param wing:
        :param u1:
        :param v1:
        :param u2:
        :param v2:
        :param rshape:
        :param build:

        :return:
        """
        return create_wing_part_by_params('spar', name, wing, u1, v1, u2, v2,
                                          rshape, build)

    @staticmethod
    def by_points(name, wing, p1, p2, rshape=None, build=True):
        """
        Create a spar by points.

        :param name:
        :param wing:
        :param p1:
        :param p2:
        :param rshape:
        :param build:

        :return:
        """
        return create_wing_part_by_points('spar', name, wing, p1, p2,
                                          rshape, build)

    # @staticmethod
    # def between_geom(name, wing, geom1, geom2, rshape, tol=None, angle=None,
    #                  assy=None):
    #     """
    #     Create a spar between geometry.
    #
    #     :param name:
    #     :param wing:
    #     :param geom1:
    #     :param geom2:
    #     :param rshape:
    #     :param float tol:
    #     :param float angle:
    #     :param assy: Part assembly by name or instance. If *None* is
    #         provided then the active assembly will be used.
    #
    #     :return:
    #     """
    #     return create_wing_part_between_geom('spar', name, wing, geom1, geom2,
    #                                          rshape, tol,
    #                                          angle, assy)
    #
    # @staticmethod
    # def by_sref(name, wing, rshape, p1, p2, tol=None, angle=None, assy=None):
    #     """
    #     Create a spar using a reference surface only.
    #
    #     :param name:
    #     :param wing:
    #     :param rshape:
    #     :param p1:
    #     :param p2:
    #     :param float tol:
    #     :param float angle:
    #     :param assy: Part assembly by name or instance. If *None* is
    #         provided then the active assembly will be used.
    #
    #     :return:
    #     """
    #     return create_wing_part_by_sref('spar', name, wing, rshape, p1, p2, tol,
    #                                     angle, assy)


class CreateRib(object):
    """
    Rib creator.
    """

    @staticmethod
    def by_parameters(name, wing, u1, v1, u2, v2, rshape=None, build=True):
        """
        Create a rib by wing parameters.

        :param name:
        :param wing:
        :param u1:
        :param v1:
        :param u2:
        :param v2:
        :param rshape:
        :param build:

        :return:
        """
        return create_wing_part_by_params('rib', name, wing, u1, v1, u2, v2,
                                          rshape, build)

    @staticmethod
    def by_points(name, wing, p1, p2, rshape=None, build=True):
        """
        Create a rib by points.

        :param name:
        :param wing:
        :param p1:
        :param p2:
        :param rshape:
        :param build:

        :return:
        """
        return create_wing_part_by_points('rib', name, wing, p1, p2, rshape,
                                          build)

        # @staticmethod
        # def between_geom(name, wing, geom1, geom2, rshape, tol=None, angle=None,
        #                  assy=None):
        #     """
        #     Create a rib between geometry.
        #
        #     :param name:
        #     :param wing:
        #     :param geom1:
        #     :param geom2:
        #     :param rshape:
        #     :param float tol:
        #     :param float angle:
        #     :param assy: Part assembly by name or instance. If *None* is
        #         provided then the active assembly will be used.
        #
        #     :return:
        #     """
        #     return create_wing_part_between_geom('rib', name, wing, geom1, geom2,
        #                                          rshape, tol,
        #                                          angle, assy)
        #
        # @staticmethod
        # def by_sref(name, wing, rshape, p1, p2, tol=None, angle=None, assy=None):
        #     """
        #     Create a rib using a reference surface only.
        #
        #     :param name:
        #     :param wing:
        #     :param rshape:
        #     :param p1:
        #     :param p2:
        #     :param float tol:
        #     :param float angle:
        #     :param assy: Part assembly by name or instance. If *None* is
        #         provided then the active assembly will be used.
        #
        #     :return:
        #     """
        #     return create_wing_part_by_sref('rib', name, wing, rshape, p1, p2, tol,
        #                                     angle, assy)


class CreateBulkhead(object):
    """
    Bulkhead creation.
    """

    @staticmethod
    def by_sref(name, fuselage, rshape, build=True):
        """
        Create a bulkhead by reference shape.

        :param name:
        :param fuselage:
        :param rshape:
        :param build:

        :return:
        """
        return create_bulkhead_by_sref(name, fuselage, rshape, build)


class CreateFloor(object):
    """
    Floor creation.
    """

    @staticmethod
    def by_sref(name, fuselage, rshape, build=True):
        """
        Create a floor by reference shape.

        :param name:
        :param fuselage:
        :param rshape:
        :param build:

        :return:
        """
        return create_floor_by_sref(name, fuselage, rshape, build)


class CreateFrame(object):
    """
    Frame creation.
    """

    @staticmethod
    def by_sref(name, fuselage, rshape, height):
        """
        Create a frame by reference shape.

        :param name:
        :param fuselage:
        :param rshape:
        :param height:

        :return:
        """
        return create_frame_by_sref(name, fuselage, rshape, height)


class CreatePart(object):
    """
    Part creator.
    """
    spar = CreateSpar()
    rib = CreateRib()
    bulkhead = CreateBulkhead()
    floor = CreateFloor()
    frame = CreateFrame()

    # fuse_skin = CreateSkin()
    # wall = CreateWall()

    @staticmethod
    def surface_part(name, rshape, *bodies):
        """
        Create a surface frame.

        :param str name: Part name.
        :param surface_like rshape: Part reference shape.
        :param bodies:

        :return: Surface frame or *None* if method fails.
        :return: :class:`.SurfacePart`
        """
        return create_surface_part(name, rshape, *bodies)