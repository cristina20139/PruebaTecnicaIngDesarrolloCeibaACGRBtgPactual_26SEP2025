import { type RouteConfig, index, route } from "@react-router/dev/routes";

export default [
  index("routes/home.tsx"),
  route("fondos", "routes/fondos.tsx"), // 👈 agrega esta línea
  route("crear-fondo", "routes/crearFondo.tsx"), // 👈 nueva ruta para Crear Fondo
  route("suscribir-fondo", "routes/suscribirFondo.tsx"), // 👈 nueva ruta para Suscribirse a Fondo
  route("clientes", "routes/clientes.tsx"), // 👈 nueva ruta para listar Clientes


] satisfies RouteConfig;
