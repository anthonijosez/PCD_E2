// Ejecuta el motor de cálculo REAL del aplicativo (extraído de Aplicativo_web.html)
const fs = require('fs');
const M = require('./motor.js');
const Med = require('./medicion.js');
function horario(spec){ const h=new Array(24).fill(0);
  spec.split(',').forEach(r=>{const [a,b]=r.split('-').map(Number); for(let i=a;i<=(b??a);i++) h[i]=1;}); return h; }
const casos = JSON.parse(fs.readFileSync('casos.json','utf8'));
const salida = casos.map(c => {
  const p = M.crearProyecto('Caso '+c.id, 'Equipo 2', '02/10/2026', c.contexto);
  c.cargas.forEach(([d,n,w,hs]) => p.cargas.push(M.crearCarga(d,n,w,horario(hs))));
  let med=null;
  if (c.csv) { med = Med.perfilDesdeHojaDeDatos(fs.readFileSync(c.csv,'utf8')); p.perfilMedidoW = med.perfilW; }
  const r = M.calcularResultadosProyecto(p, {diasOperacionMes:c.dm, diasOperacionAnio:c.da, costoUnitarioCU:c.cu, horaInicioDia:6, horaFinDia:18});
  return { id:c.id, ...r, medicion: med && {totalLecturas:med.totalLecturas, filasDescartadas:med.filasDescartadas, avisos:med.avisos} };
});
fs.writeFileSync('resultados_app.json', JSON.stringify(salida,null,1));
console.log('ok', salida.length);
