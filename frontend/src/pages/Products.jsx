import { useEffect, useState } from "react";
import api from "../services/api";

export default function Products() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    api.get("/products").then((res) => setProducts(res.data));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl mb-4">Produtos</h1>
      <ul>
        {products.map((p) => (
          <li key={p.id}>
            {p.name} - R$ {p.price} - Categoria: {p.category_id}
          </li>
        ))}
      </ul>
    </div>
  );
}
