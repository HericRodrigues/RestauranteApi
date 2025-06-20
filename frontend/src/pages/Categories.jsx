import { useEffect, useState } from "react";
import api from "../services/api";

export default function Categories() {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    api.get("/categories").then((res) => setCategories(res.data));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl mb-4">Categorias</h1>
      <ul>
        {categories.map((c) => (
          <li key={c.id}>{c.name}</li>
        ))}
      </ul>
    </div>
  );
}
