from __future__ import print_function

import time

from asap.graphics import Viewer
from asap.io import ImportVSP
from asap.structure import CreatePart

# Import model
fn = r'.\test_io\777-200LR_mod_vsp350_sref.stp'
ImportVSP.step_file(fn)

# Get components.
wing = ImportVSP.get_body('Wing')
fuselage = ImportVSP.get_body('Fuselage')

start = time.time()
# Spars
fspar = CreatePart.spar.by_parameters('fspar', wing, 0.15, 0.05, 0.15, 0.925)
rspar = CreatePart.spar.by_parameters('rspar', wing, 0.65, 0.05, 0.65, 0.925)

# Bulkheads
bh1 = CreatePart.bulkhead.by_sref('bh1', fuselage, fspar.rshape)
bh2 = CreatePart.bulkhead.by_sref('bh2', fuselage, rspar.rshape)

# Join
fspar.join(bh1)
rspar.join(bh2)

for part in [fspar, rspar, bh1, bh2]:
    part.mesh(12., quad_dominated=False)
Viewer.add_meshes(bh1, bh2, fspar, rspar)
Viewer.show_mesh()