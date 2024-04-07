import torch
import numpy as np

# n0 - 2D tensor, is the analitically computed function to be reproduced with particle ensemble
# n0 is assumed to be strictly positive (> 0) at all points
# N_min - number of particles for minimal value of n0
# xx - tensor, set of points along X
# yy - tensor, set of points along Y
def get_particles(n0,N_min,xx,yy):
    n0_min = torch.min(n0)
    n0_max = torch.max(n0)
    n0_total = torch.sum(n0)
    #N = (n0_total/n0_min)*N_min
    w = n0_max/n0_min/N_min       # single particle weight: maximum to minimum ratio is represented by 10 particles

    particles = []
    Npx = 50

    # xm = (xx[:-1] + xx[1:]) * 0.5
    # ym = (yy[:-1] + yy[1:]) * 0.5
    xm = np.linspace(xx[:-1],xx[1:],Npx)
    ym = np.linspace(yy[:-1],yy[1:],Npx)

    for i,x in enumerate(xx):
        for j,y in enumerate(yy):
              N_ij = int(np.ceil(n0[i][j].numpy()/w).numpy())
              for k in range(N_ij):
                  particles.append([x,y])

    particles = torch.tensor(particles)
    return particles

