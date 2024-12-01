FIGURE GENERATOR

fgmk3:
    Mandatory:
      Figure Number, Title(s), Config or {}, data[x0, y0, xlabel, ylabel]
    Optional:
      x: x values for data sets
      y: y values for data sets
      lbl: Label for data sets
      lc: Color for data sets
      figt: Figure text
      grid: Enable grid (default: 1)
      splots: Number of subplots
      ptype: Type of Plot
      dim: 1x2 Tuple for figure dimensions

toSheet:
    Mandatory:
      Excel Name, Sheet Name
    Optional:
      Any array or numeric value in dictionary form, such as Var=[21] or Var=Var

fgmk, fgmk2, and hgmk2 are deprecated as of 2024-11-27