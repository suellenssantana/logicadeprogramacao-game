class EntityMediator:
    @staticmethod
    def verify_collision(entity_list):
        for i, ent1 in enumerate(entity_list):
            for ent2 in entity_list[i + 1:]:
                if ent1.rect.colliderect(ent2.rect):
                    ent1.health -= ent2.damage
                    ent2.health -= ent1.damage

    @staticmethod
    def verify_health(entity_list):
        for ent in entity_list[:]:
            if ent.health <= 0:
                entity_list.remove(ent)