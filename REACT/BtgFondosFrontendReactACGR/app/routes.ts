import { type RouteConfig, index, route } from "@react-router/dev/routes";

export default [
  index("routes/home.tsx"),
  route("fondos", "routes/fondos.tsx"), // 👈 agrega esta línea
] satisfies RouteConfig;
