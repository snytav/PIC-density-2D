import torch
import numpy as np

# n0 - 2D tensor, is the analitically computed function to be reproduced with particle ensemble
# n0 is assumed to be strictly positive (> 0) at all points
# N_min - number of particles for minimal value of n0
# xx - tensor, set of points along X
# yy - tensor, set of points along Y
def get_particles(n0,N_min,xx,yy):
    n0_min = torch.min(n0)
    n0_total = torch.sum(n0)
    N = (n0_total/n0_min)*N_min

    particles = []

    #xm = (xx[:-1]+xx[1:])*0.
    Npx = 50
    #xm = np.linspace(xx[0],xx[-1],Npx)
    xm = np.loadtxt('uniform.txt')
    ym = np.linspace(yy[0],yy[-1],Npx)
   # ym = (yy[:-1] + yy[1:]) * 0.5
    for i,x in enumerate(xx):
        for j,y in enumerate(yy):
              # N_ij = int(np.ceil(n0[i][j].numpy()/n0_min *N_min).numpy())
              # for k in range(N_ij):
              particles.append([x, y])
              if i == 0 and j == 0:
                  particles.append([x,y])
        qq = 0

    particles = torch.tensor(particles)
    return particles

