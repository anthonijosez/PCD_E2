# Cálculo manual (valores obtenidos a mano con E = Σ N·P·h) frente a la salida del aplicativo
import json, csv
app = {r['id']: r for r in json.load(open('resultados_app.json'))}
manual = {
 1: dict(potenciaInstaladaW=290, demandaMaximaW=290, horaDemandaMaximaH=19, energiaDiariaKWh=4.2, energiaMensualKWh=126, energiaAnualKWh=1533,
         costoDiario=3780, costoMensual=113400, costoAnual=1379700, clasificacion=['mixta','nocturna','nocturna']),
 2: dict(potenciaInstaladaW=1500, demandaMaximaW=1380, horaDemandaMaximaH=0, energiaDiariaKWh=14.52, energiaMensualKWh=435.6, energiaAnualKWh=5227.2,
         costoDiario=12342, costoMensual=370260, costoAnual=4443120, clasificacion=['nocturna','diurna','mixta']),
 3: dict(potenciaInstaladaW=5860, demandaMaximaW=5860, horaDemandaMaximaH=9, energiaDiariaKWh=55.52, energiaMensualKWh=1221.44, energiaAnualKWh=14657.28,
         costoDiario=55520, costoMensual=1221440, costoAnual=14657280, clasificacion=['diurna','diurna','mixta','mixta']),
 4: dict(potenciaInstaladaW=750, demandaMaximaW=750, horaDemandaMaximaH=6, energiaDiariaKWh=1.5, energiaMensualKWh=45, energiaAnualKWh=547.5,
         costoDiario=0, costoMensual=0, costoAnual=0, clasificacion=['diurna'], advertenciaCU0=True),
 5: dict(potenciaInstaladaW=1350, demandaMaximaW=1500, horaDemandaMaximaH=18, energiaDiariaKWh=10.0, energiaMensualKWh=300, energiaAnualKWh=3650,
         costoDiario=9000, costoMensual=270000, costoAnual=3285000, clasificacion=['mixta','nocturna'], fuentePerfil='medido',
         EdEstimada=8.4, diferenciaPorcentaje=19.047619, totalLecturas=144, filasDescartadas=2),
}
filas=[]; fallos=0
for cid, m in manual.items():
    a = app[cid]
    for k, vm in m.items():
        if k=='clasificacion': va=a['clasificacionCargas']
        elif k in ('EdEstimada','diferenciaPorcentaje'): va=a['comparacionPerfiles'][k]
        elif k in ('totalLecturas','filasDescartadas'): va=a['medicion'][k]
        else: va=a[k]
        if isinstance(vm,(int,float)) and not isinstance(vm,bool):
            dif=va-vm; rel=(dif/vm*100) if vm else 0.0
            ok=abs(dif)<=1e-6*max(1,abs(vm)) or abs(rel)<1e-4
            filas.append([cid,k,vm,round(va,6),round(dif,6),f"{rel:.4f}",'OK' if ok else 'FALLA'])
        else:
            ok = va==vm
            filas.append([cid,k,vm,va,'-','-','OK' if ok else 'FALLA'])
        fallos += 0 if ok else 1
with open('comparacion_manual_vs_app.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['caso','indicador','manual','aplicativo','diferencia','diferencia_%','resultado']); w.writerows(filas)
for r in filas: print(r)
print('FALLAS:',fallos,'de',len(filas))
print('avisos caso 5:', app[5]['medicion']['avisos'])
