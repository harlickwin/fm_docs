# Game Mechanics Pattern Search Results

## PCG Random Number Generator

No PCG algorithm found (may use different RNG)

## Drop Chance Tables

Found 18 potential drop tables:

### Line 1035832
```c
        fVar14 = (float)func_0x065d3e2c(uVar1,uVar2,uVar3,uStack_4c,uStack_48,uStack_44,
                                        *(undefined4 *)(param_1 + 0x18),0);
      }
      else {
        fVar14 = *(float *)(param_1 + 0x18);
      }
      if (cRam0725b02f == '\0') {
        thunk_FUN_01c85508(&DAT_0707620c);
        cRam0725b02f = '\x01';
      }
      if (*(int *)(_DAT_0707620c + 0x74) == 0) {
        thunk_FUN_01cddfe8();
      }
      fVar15 = (float)puVar4[4] + (float)puVar4[4];
      fVar5 = (float)puVar4[3] + (float)puVar4[3];
      fVar16 = (float)puVar4[5] + (float)puVar4[5];
      fVar13 = fVar15;
      if (0x7f800000 < (uint)ABS(fVar15)) {
        fVar13 = fVar5;
      }
      if (fVar15 < fVar5) {
        fVar13 = fVar5;
      }
      fVar5 = fVar16;
      if (fVar16 < fVar13) {
        fVar5 = fVar13;
      }
      if (0x7f800000 < (uint)ABS(fVar16)) {
        fVar5 = fVar13;
      }
      fVar15 = (float)func_0x065d1f94(*(undefined4 *)(param_1 + 0x1c),fVar5,0);

```

### Line 1043630
```c
        if (cRam0725b02b == '\0') {
          thunk_FUN_01c85508(&DAT_0707620c);
          cRam0725b02b = '\x01';
        }
        if (*(int *)(_DAT_0707620c + 0x74) == 0) {
          thunk_FUN_01cddfe8();
        }
        dVar16 = (double)func_0x0585f280(SUB84((double)fVar15,0),
                                         (int)((ulonglong)(double)fVar15 >> 0x20),0,0x40000000,0);
        cVar1 = (char)param_1[0xe];
        fVar15 = (float)dVar16;
      }
      else {
        cVar1 = '\x01';
      }
      fVar10 = (float)param_1[7];
      fVar11 = (float)param_1[6];
      fVar15 = fVar10 + fVar15 * fVar11;
      iVar13 = (int)fVar15;
      if (fVar15 == INFINITY) {
        iVar13 = -0x80000000;
      }
      if (iVar13 <= param_2) {
        iVar13 = param_2;
      }
      if (cVar1 == '\0') {
        if (cRam0725b02b == '\0') {
          thunk_FUN_01c85508(&DAT_0707620c);
          cRam0725b02b = '\x01';
        }
        if (*(int *)(_DAT_0707620c + 0x74) == 0) {

```

### Line 1043631
```c
          thunk_FUN_01c85508(&DAT_0707620c);
          cRam0725b02b = '\x01';
        }
        if (*(int *)(_DAT_0707620c + 0x74) == 0) {
          thunk_FUN_01cddfe8();
        }
        dVar16 = (double)func_0x0585f280(SUB84((double)fVar15,0),
                                         (int)((ulonglong)(double)fVar15 >> 0x20),0,0x40000000,0);
        cVar1 = (char)param_1[0xe];
        fVar15 = (float)dVar16;
      }
      else {
        cVar1 = '\x01';
      }
      fVar10 = (float)param_1[7];
      fVar11 = (float)param_1[6];
      fVar15 = fVar10 + fVar15 * fVar11;
      iVar13 = (int)fVar15;
      if (fVar15 == INFINITY) {
        iVar13 = -0x80000000;
      }
      if (iVar13 <= param_2) {
        iVar13 = param_2;
      }
      if (cVar1 == '\0') {
        if (cRam0725b02b == '\0') {
          thunk_FUN_01c85508(&DAT_0707620c);
          cRam0725b02b = '\x01';
        }
        if (*(int *)(_DAT_0707620c + 0x74) == 0) {
          thunk_FUN_01cddfe8();

```

### Line 1043650
```c
        iVar13 = -0x80000000;
      }
      if (iVar13 <= param_2) {
        iVar13 = param_2;
      }
      if (cVar1 == '\0') {
        if (cRam0725b02b == '\0') {
          thunk_FUN_01c85508(&DAT_0707620c);
          cRam0725b02b = '\x01';
        }
        if (*(int *)(_DAT_0707620c + 0x74) == 0) {
          thunk_FUN_01cddfe8();
        }
        dVar16 = (double)func_0x0585f280(SUB84((double)fVar14,0),
                                         (int)((ulonglong)(double)fVar14 >> 0x20),0,0x40000000,0);
        fVar11 = (float)param_1[6];
        fVar10 = (float)param_1[7];
        fVar14 = (float)dVar16;
      }
      fVar10 = fVar10 + fVar14 * fVar11;
      iVar12 = (int)fVar10;
      if (fVar10 == INFINITY) {
        iVar12 = -0x80000000;
      }
      if (param_3 <= iVar12) {
        iVar12 = param_3;
      }
      if (iVar13 <= iVar12) {
        iVar6 = *param_1;
        do {
          iVar3 = param_1[9];

```

### Line 1043651
```c
      }
      if (iVar13 <= param_2) {
        iVar13 = param_2;
      }
      if (cVar1 == '\0') {
        if (cRam0725b02b == '\0') {
          thunk_FUN_01c85508(&DAT_0707620c);
          cRam0725b02b = '\x01';
        }
        if (*(int *)(_DAT_0707620c + 0x74) == 0) {
          thunk_FUN_01cddfe8();
        }
        dVar16 = (double)func_0x0585f280(SUB84((double)fVar14,0),
                                         (int)((ulonglong)(double)fVar14 >> 0x20),0,0x40000000,0);
        fVar11 = (float)param_1[6];
        fVar10 = (float)param_1[7];
        fVar14 = (float)dVar16;
      }
      fVar10 = fVar10 + fVar14 * fVar11;
      iVar12 = (int)fVar10;
      if (fVar10 == INFINITY) {
        iVar12 = -0x80000000;
      }
      if (param_3 <= iVar12) {
        iVar12 = param_3;
      }
      if (iVar13 <= iVar12) {
        iVar6 = *param_1;
        do {
          iVar3 = param_1[9];
          iVar9 = param_8 + iVar13;

```

### Line 1064575
```c
    func_0x0686cf14(&uStack_50,iVar1,uStack_50,fStack_4c,uStack_48,uStack_44,0);
    if (param_2[9] == 0) {
                    // WARNING: Subroutine does not return
      thunk_FUN_01ccb208();
    }
    fVar3 = (float)func_0x06918418(param_2[9],0);
    if (fVar3 != 0.0) {
      if (param_2[9] == 0) {
                    // WARNING: Subroutine does not return
        thunk_FUN_01ccb208();
      }
      uStack_48 = func_0x06918418(param_2[9],0);
    }
    fVar4 = (float)func_0x0692db24(param_2);
    fVar5 = (float)func_0x0692d50c(param_2);
    fVar10 = (float)param_2[7];
    fVar6 = (float)param_2[6];
    fVar7 = (float)param_2[5];
    fVar9 = (float)param_2[4];
    fVar3 = fVar10;
    if (fVar10 < fVar6) {
      fVar3 = fVar6;
    }
    fVar8 = fVar9;
    if (fVar3 - fVar7 < fVar9) {
      fVar8 = fVar3 - fVar7;
    }
    if (fVar10 <= fVar6) {
      fVar4 = fVar4 - fVar5 * fVar7;
      if (fVar9 < fVar10) {
        fVar8 = fVar10;

```

### Line 1064576
```c
    if (param_2[9] == 0) {
                    // WARNING: Subroutine does not return
      thunk_FUN_01ccb208();
    }
    fVar3 = (float)func_0x06918418(param_2[9],0);
    if (fVar3 != 0.0) {
      if (param_2[9] == 0) {
                    // WARNING: Subroutine does not return
        thunk_FUN_01ccb208();
      }
      uStack_48 = func_0x06918418(param_2[9],0);
    }
    fVar4 = (float)func_0x0692db24(param_2);
    fVar5 = (float)func_0x0692d50c(param_2);
    fVar10 = (float)param_2[7];
    fVar6 = (float)param_2[6];
    fVar7 = (float)param_2[5];
    fVar9 = (float)param_2[4];
    fVar3 = fVar10;
    if (fVar10 < fVar6) {
      fVar3 = fVar6;
    }
    fVar8 = fVar9;
    if (fVar3 - fVar7 < fVar9) {
      fVar8 = fVar3 - fVar7;
    }
    if (fVar10 <= fVar6) {
      fVar4 = fVar4 - fVar5 * fVar7;
      if (fVar9 < fVar10) {
        fVar8 = fVar10;
      }

```

### Line 1064577
```c
                    // WARNING: Subroutine does not return
      thunk_FUN_01ccb208();
    }
    fVar3 = (float)func_0x06918418(param_2[9],0);
    if (fVar3 != 0.0) {
      if (param_2[9] == 0) {
                    // WARNING: Subroutine does not return
        thunk_FUN_01ccb208();
      }
      uStack_48 = func_0x06918418(param_2[9],0);
    }
    fVar4 = (float)func_0x0692db24(param_2);
    fVar5 = (float)func_0x0692d50c(param_2);
    fVar10 = (float)param_2[7];
    fVar6 = (float)param_2[6];
    fVar7 = (float)param_2[5];
    fVar9 = (float)param_2[4];
    fVar3 = fVar10;
    if (fVar10 < fVar6) {
      fVar3 = fVar6;
    }
    fVar8 = fVar9;
    if (fVar3 - fVar7 < fVar9) {
      fVar8 = fVar3 - fVar7;
    }
    if (fVar10 <= fVar6) {
      fVar4 = fVar4 - fVar5 * fVar7;
      if (fVar9 < fVar10) {
        fVar8 = fVar10;
      }
      fVar8 = fVar7 + fVar8;

```

### Line 1064661
```c
    func_0x0686cf14(&fStack_50,iVar1,fStack_50,fStack_4c,uStack_48,fStack_44,0);
    if (param_2[9] == 0) {
                    // WARNING: Subroutine does not return
      thunk_FUN_01ccb208();
    }
    fVar3 = (float)func_0x069184d8(param_2[9],0);
    if (fVar3 != 0.0) {
      if (param_2[9] == 0) {
                    // WARNING: Subroutine does not return
        thunk_FUN_01ccb208();
      }
      fStack_44 = (float)func_0x069184d8(param_2[9],0);
    }
    fVar4 = (float)func_0x0692db24(param_2);
    fVar5 = (float)func_0x0692d50c(param_2);
    fVar10 = (float)param_2[7];
    fVar6 = (float)param_2[6];
    fVar7 = (float)param_2[5];
    fVar9 = (float)param_2[4];
    fVar3 = fVar10;
    if (fVar10 < fVar6) {
      fVar3 = fVar6;
    }
    fVar8 = fVar9;
    if (fVar3 - fVar7 < fVar9) {
      fVar8 = fVar3 - fVar7;
    }
    if (fVar10 <= fVar6) {
      fVar4 = fVar4 - fVar5 * fVar7;
      if (fVar9 < fVar10) {
        fVar8 = fVar10;

```

### Line 1064662
```c
    if (param_2[9] == 0) {
                    // WARNING: Subroutine does not return
      thunk_FUN_01ccb208();
    }
    fVar3 = (float)func_0x069184d8(param_2[9],0);
    if (fVar3 != 0.0) {
      if (param_2[9] == 0) {
                    // WARNING: Subroutine does not return
        thunk_FUN_01ccb208();
      }
      fStack_44 = (float)func_0x069184d8(param_2[9],0);
    }
    fVar4 = (float)func_0x0692db24(param_2);
    fVar5 = (float)func_0x0692d50c(param_2);
    fVar10 = (float)param_2[7];
    fVar6 = (float)param_2[6];
    fVar7 = (float)param_2[5];
    fVar9 = (float)param_2[4];
    fVar3 = fVar10;
    if (fVar10 < fVar6) {
      fVar3 = fVar6;
    }
    fVar8 = fVar9;
    if (fVar3 - fVar7 < fVar9) {
      fVar8 = fVar3 - fVar7;
    }
    if (fVar10 <= fVar6) {
      fVar4 = fVar4 - fVar5 * fVar7;
      if (fVar9 < fVar10) {
        fVar8 = fVar10;
      }

```

## Comparison Chains (Rarity Determination)

Found 50 comparison chains:

### Line 4247
```c
LAB_01cde350:
        bVar5 = false;
        ClearExclusiveLocal();
      }
      DataMemoryBarrier(0xb);
      if (bVar5) {
        return;
      }
      if (iVar6 == iVar3) {
        return;
      }
      if (*piVar10 == 1) {
        DataMemoryBarrier(0xb);
        while (bVar5 = (bool)hasExclusiveAccess(piVar10), !bVar5) {
          if (*piVar10 != 1) goto LAB_01cde3a0;
        }
        *piVar10 = 1;
      }
      else {
LAB_01cde3a0:
        piVar8 = (int *)(param_1 + 0x6c);
        ClearExclusiveLocal();
        DataMemoryBarrier(0xb);
        while (*piVar8 == 0) {
          DataMemoryBarrier(0xb);
          while (bVar5 = (bool)hasExclusiveAccess(piVar8), !bVar5) {
            if (*piVar8 != 0) goto LAB_01cde424;

```

### Line 24654
```c
LAB_01cde350:
        bVar5 = false;
        ClearExclusiveLocal();
      }
      DataMemoryBarrier(0xb);
      if (bVar5) {
        return;
      }
      if (iVar6 == iVar3) {
        return;
      }
      if (*piVar10 == 1) {
        DataMemoryBarrier(0xb);
        while (bVar5 = (bool)hasExclusiveAccess(piVar10), !bVar5) {
          if (*piVar10 != 1) goto LAB_01cde3a0;
        }
        *piVar10 = 1;
      }
      else {
LAB_01cde3a0:
        piVar8 = (int *)(param_1 + 0x6c);
        ClearExclusiveLocal();
        DataMemoryBarrier(0xb);
        while (*piVar8 == 0) {
          DataMemoryBarrier(0xb);
          while (bVar5 = (bool)hasExclusiveAccess(piVar8), !bVar5) {
            if (*piVar8 != 0) goto LAB_01cde424;

```

### Line 26205
```c
        uStack_78._4_4_ = (uint)((byte)uStack_78 >> 1);
      }
      uVar4 = uStack_78._4_4_;
      uStack_78 = uVar10;
      FUN_01d9f734(&uStack_40,uVar6,uVar4);
      if ((uStack_78 & 1) != 0) {
        FUN_01d9f474(uStack_70);
      }
      if ((uStack_88 & 1) != 0) {
        FUN_01d9f474(uStack_80);
      }
      if ((uStack_98 & 1) != 0) {
        FUN_01d9f474(uStack_90);
      }
      if ((abStack_a4[0] & 1) != 0) {
        FUN_01d9f474(uStack_9c);
      }
      if (((byte)uStack_40 & 1) == 0) {
        uStack_38 = (uint)&uStack_40 | 1;
      }
      uVar2 = FUN_01ccc494(uStack_38);
                    // WARNING: Subroutine does not return
      FUN_01ccb164(uVar2,0);
    }
  }
  return iVar8;
}




```

### Line 34874
```c
        iVar2 = *(int *)(*(int *)(param_1 + 0x18) + iVar11);
        uVar9 = *(uint *)(iVar2 + 4);
        iVar2 = FUN_01ce1c28(iVar2,1);
        FUN_01ce21b0();
        uVar9 = uVar9 & 0x20000000;
        if ((int)*(uint *)(iVar2 + 0x14) < 0) {
          bVar12 = *(int *)(iVar2 + 0x30) != 0;
          uVar1 = 0;
          if (bVar12) {
            uVar1 = *(ushort *)(iVar2 + 0xbd);
          }
          if (!bVar12 || (uVar1 & 8) == 0) {
            piVar4 = (int *)(param_3 + iVar11);
            iVar3 = *piVar4;
            if (uVar9 == 0) {
              if (iVar3 == 0) {
                iVar2 = *(int *)(iVar2 + 0x80);
                piVar5 = (int *)((int)piVar5 - (iVar2 - 1U & 0xfffffff8));
                *(int **)((int)piStack_30 + iVar11) = piVar5;
                FUN_01d4bccc(piVar5,iVar2 + -8);
                goto LAB_01ce0544;
              }
            }
            else if (iVar3 == 0) {
              uVar6 = thunk_FUN_01cc4794(iVar2);
              FUN_01c88640(piVar4,uVar6);
              iVar3 = *piVar4;

```

### Line 35166
```c
LAB_01cde350:
        bVar5 = false;
        ClearExclusiveLocal();
      }
      DataMemoryBarrier(0xb);
      if (bVar5) {
        return;
      }
      if (iVar6 == iVar3) {
        return;
      }
      if (*piVar10 == 1) {
        DataMemoryBarrier(0xb);
        while (bVar5 = (bool)hasExclusiveAccess(piVar10), !bVar5) {
          if (*piVar10 != 1) goto LAB_01cde3a0;
        }
        *piVar10 = 1;
      }
      else {
LAB_01cde3a0:
        piVar8 = (int *)(param_1 + 0x6c);
        ClearExclusiveLocal();
        DataMemoryBarrier(0xb);
        while (*piVar8 == 0) {
          DataMemoryBarrier(0xb);
          while (bVar5 = (bool)hasExclusiveAccess(piVar8), !bVar5) {
            if (*piVar8 != 0) goto LAB_01cde424;

```

### Line 38102
```c
    piVar4 = (int *)0x0;
  }
  else {
    iVar5 = param_3 - param_2;
    iVar6 = *(int *)(param_5 + 0xc) - (param_4 - param_2);
    if (iVar6 == 0 || *(int *)(param_5 + 0xc) < param_4 - param_2) {
      iVar6 = 0;
    }
    if ((iVar5 < 1) ||
       (iVar1 = (**(code **)(*param_1 + 0x30))(param_1,param_2,iVar5), piVar4 = (int *)0x0,
       iVar1 == iVar5)) {
      if (0 < iVar6) {
        uVar2 = FUN_01c8e538(abStack_30,iVar6,param_6);
        uVar3 = uStack_28;
        if ((abStack_30[0] & 1) == 0) {
          uVar3 = uVar2 | 1;
        }
        iVar5 = (**(code **)(*param_1 + 0x30))(param_1,uVar3,iVar6);
        if ((abStack_30[0] & 1) != 0) {
          FUN_01d9f474(uStack_28);
        }
        if (iVar5 != iVar6) {
          return (int *)0x0;
        }
      }
      param_4 = param_4 - param_3;
      if ((0 < param_4) &&

```

### Line 44598
```c
            }
            else {
              piVar15 = (int *)*param_2;
              iVar4 = (int)piVar11 - (int)piVar15 >> 2;
              uVar14 = iVar4 + 1;
              if (0x3fffffff < uVar14) goto LAB_01ca5154;
              uVar3 = (int)param_2[2] - (int)piVar15;
              uVar1 = (int)uVar3 >> 1;
              if (uVar14 < uVar1) {
                uVar14 = uVar1;
              }
              if (0x7ffffffb < uVar3) {
                uVar14 = 0x3fffffff;
              }
              if (uVar14 == 0) {
                iVar6 = 0;
              }
              else {
                if (0x3fffffff < uVar14) goto LAB_01ca5170;
                iVar6 = FUN_01d9f494(uVar14 << 2);
              }
              piVar8 = (int *)(iVar6 + iVar4 * 4);
              *piVar8 = iVar5;
              piVar10 = piVar8;
              if (piVar11 != piVar15) {
                do {
                  piVar11 = piVar11 + -1;

```

### Line 53347
```c
  if (iRam0726188c != 0) {
    iVar2 = iRam0726188c;
    do {
      iVar1 = *(int *)(iVar2 + 0x24);
      bVar3 = iVar1 == *param_1;
      if (bVar3) {
        iVar1 = *(int *)(iVar2 + 0x28);
      }
      if (bVar3 && iVar1 == param_1[0x18]) {
        FUN_01c86f44(auStack_1c);
        iVar1 = extraout_r1;
        if (param_2 != 0) {
          iVar1 = *(int *)(iVar2 + 0x18);
        }
        if (param_2 == 0 || iVar1 == 0) {
          return false;
        }
        if ((param_3 != 1) && (iVar1 == 1)) {
          return false;
        }
        return param_3 == 2 || iVar1 != 2;
      }
      iVar2 = *(int *)(iVar2 + 0x30);
    } while (iVar2 != 0);
  }
  FUN_01c86f44(auStack_1c);
  return true;
}



```

### Line 54534
```c
    *(undefined4 *)puVar4 = 0;
    *(undefined4 *)((int)puVar4 + 4) = 0;
    *(undefined4 *)(puVar4 + 1) = 0;
    *(undefined4 *)(param_1 + 1) = uVar3;
    *param_1 = uVar7;
    if ((abStack_70[0] & 1) != 0) {
      FUN_01d9f474(uStack_68);
    }
    if ((uStack_48 & 1) != 0) {
      FUN_01d9f474(uStack_40);
    }
    if ((uStack_58 & 1) != 0) {
      FUN_01d9f474(uStack_50);
    }
    if ((abStack_64[0] & 1) == 0) goto LAB_01cbcf30;
  }
  FUN_01d9f474(uStack_5c);
LAB_01cbcf30:
  if ((abStack_38[0] & 1) != 0) {
    FUN_01d9f474(uStack_30);
  }
  if ((abStack_2c[0] & 1) != 0) {
    FUN_01d9f474(uStack_24);
  }
  return;
}


```

### Line 56560
```c
    uVar2 = (byte)uStack_30 & 1;
    uVar6 = (uint)((byte)uStack_30 >> 1);
    uVar4 = uStack_30._4_4_;
  }
  uVar8 = uVar4;
  if (uVar2 == 0) {
    uVar8 = uVar6;
  }
  if ((uVar8 == 0) || (iVar5 = 0, iStack_24 != 0)) {
    uVar4 = FUN_01c8cc14(&bStack_50,&UNK_00d82fbf);
    uVar6 = uStack_4c;
    if ((bStack_50 & 1) == 0) {
      uVar6 = (uint)(bStack_50 >> 1);
    }
    if (uVar6 != 0) {
      uStack_20 = uStack_48;
      if ((bStack_50 & 1) == 0) {
        uStack_20 = uVar4 | 1;
      }
      uStack_1c = uVar6;
      FUN_01c91244(&uStack_60,&uStack_20,&puStack_38);
      if ((uStack_30 & 1) != 0) {
        FUN_01d9f474(uStack_28);
      }
      uStack_30 = CONCAT44(uStack_5c,uStack_60);
      uStack_28 = uStack_58;
    }

```

## Stat Calculations

### Attack Speed

Found 12 occurrences:

#### Line 512685
```c
    fVar5 = 1.0;
  }
  else {
    fVar5 = (float)thunk_FUN_0693ecc4(&uStack_10,0);
    fVar6 = (float)thunk_FUN_0693eccc(&uStack_10,0);
    fVar5 = fVar5 / fVar6;
  }
  iVar1 = *(int *)(in_stack_0000003c + 0x10);
  if ((*(ushort *)(iVar1 + 0xbd) & 1) == 0) {
    FUN_01cc1738();
    iVar1 = *(int *)(in_stack_0000003c + 0x10);

```

#### Line 766282
```c
  double dStack_28;
  
  if (param_2 == 0.0) {
    return param_1;
  }
  param_1 = param_1 / param_2;
  dVar3 = (double)modf(SUB84((double)param_1,0),(int)((ulonglong)(double)param_1 >> 0x20),&dStack_28
                      );
  if (0.0 <= param_1) {
    if (dVar3 != 0.5) {
      fVar2 = (float)floorf(param_1 + 0.5);

```

#### Line 766942
```c
  double dStack_28;
  
  if (param_2 == 0.0) {
    return param_1;
  }
  param_1 = param_1 / param_2;
  dVar3 = (double)modf(SUB84((double)param_1,0),(int)((ulonglong)(double)param_1 >> 0x20),&dStack_28
                      );
  if (0.0 <= param_1) {
    if (dVar3 != 0.5) {
      fVar2 = (float)floorf(param_1 + 0.5);

```

#### Line 867122
```c
  double dStack_28;
  
  if (param_2 == 0.0) {
    return param_1;
  }
  param_1 = param_1 / param_2;
  dVar3 = (double)modf(SUB84((double)param_1,0),(int)((ulonglong)(double)param_1 >> 0x20),&dStack_28
                      );
  if (0.0 <= param_1) {
    if (dVar3 != 0.5) {
      fVar2 = (float)floorf(param_1 + 0.5);

```

#### Line 868483
```c
  double dStack_28;
  
  if (param_2 == 0.0) {
    return param_1;
  }
  param_1 = param_1 / param_2;
  dVar3 = (double)modf(SUB84((double)param_1,0),(int)((ulonglong)(double)param_1 >> 0x20),&dStack_28
                      );
  if (0.0 <= param_1) {
    if (dVar3 != 0.5) {
      fVar2 = (float)floorf(param_1 + 0.5);

```

### Damage

No matches found

### Crit

No matches found

### Health

No matches found

## Large Constants (Config Values)

Found 100 large constants:

Most common large constants:

- `5000` appears 18 times
- `1879048186` appears 14 times
- `1879048187` appears 14 times
- `1879048188` appears 14 times
- `1879048189` appears 14 times
- `1879048190` appears 14 times
- `1879048191` appears 13 times
- `1000` appears 10 times
- `1610612754` appears 7 times
- `1879040000` appears 7 times
- `1879040001` appears 7 times
- `1879040003` appears 7 times
- `1879047669` appears 7 times
- `1879047670` appears 7 times
- `1879047671` appears 7 times
- `1879047672` appears 7 times
- `1879047673` appears 7 times
- `1879047674` appears 7 times
- `1879047675` appears 7 times
- `1879047676` appears 7 times

