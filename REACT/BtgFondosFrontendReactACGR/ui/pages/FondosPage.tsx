import { useEffect, useState } from "react";
import { listarFondos } from "../../application/usecases/ListarFondos";
import type { Fondo } from "../../domain/entidades/Fondo";

export default function FondosPage() {
  const [fondos, setFondos] = useState<Fondo[]>([]);

  useEffect(() => {
    listarFondos().then(setFondos);
  }, []);

  return (
    <div>
      <h1>Fondos disponibles</h1>
      <ul>
        {fondos.map(f => (
          <li key={f.id}>
            {f.nombre} - {f.categoria} - Mínimo: {f.monto_minimo}
          </li>
        ))}
      </ul>
    </div>
  );
}
